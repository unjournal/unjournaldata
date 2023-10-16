# Unjournal Data Dashboard
# By Julia Bottesini
#

library(shiny)
library(tidyverse)
library(RColorBrewer)
library(fmsb)
library(scales)

# Import data
df <- read_rds("shiny_explorer.rds")
# df <- read_rds("./shinyapp/DataExplorer/shiny_explorer.rds")

# create a palette with a color for each paper
color_count = df$paper_abbrev %>% unique() %>% length()
my_pal = colorRampPalette(brewer.pal(8, "Set1"))(color_count)


# create new variables
df <- df %>% 
  group_by(paper_abbrev, rating_type) %>% 
  mutate(n_evals = n(), # number of evaluators for each paper
         rating_mean = mean(est, na.rm = T)) %>%  # TODO: replace with aggreCAT functions later
  ungroup() %>%
  nest(.by = paper_abbrev) %>% 
  mutate(paper_color = my_pal) %>% # give each paper its own color
  unnest(cols = c(data))


# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("Unjournal Evaluation Data"),
  
  tabsetPanel(
    tabPanel(title = "Across Papers",
    # Sidebar with plot options
    sidebarLayout(
      sidebarPanel(

                 
                 selectInput(inputId = "RatingType",
                             label = "Rating Type:",
                             choices = df$rating_type[!grepl(x = df$rating_type, pattern = "Journal$")] %>% unique() %>% as.character(), 
                             selected = "Overall assessment",
                             multiple = F),
                 checkboxInput(inputId = "ToggleMean",
                               label = "Show aggregated rating",
                               value = FALSE),
                 checkboxInput(inputId = "ToggleRange",
                               label = "Show aggregated range",
                               value = FALSE),
                 checkboxInput(inputId = "ToggleNonAnonymous",
                               label = "Show only evals by Anon",
                               value = FALSE),
                 hr(),
                 checkboxGroupInput(
                   inputId = "IncludedPapers",
                   label = "Which Papers?",
                   choices = unique(df$paper_abbrev),
                   selected = unique(df$paper_abbrev),
                   inline = FALSE,
                   width = "200px",
                   choiceNames = NULL,
                   choiceValues = NULL
                 ),

                 width = 3
        ), fluid = F, position = "right",
        
        # Show the plot with selected info
        mainPanel(
          plotOutput(outputId = "distPlot",
                     width = "100%")
        )#/mainPanel
      )#/sideLayout
    
    
    ),#/tabPanel
    
    tabPanel(title = "Individual Papers",
             # insert shiny app here
             # Sidebar with plot options
             sidebarLayout(
               sidebarPanel(
                 
                 selectInput(inputId = "PaperName",
                             label = "Which paper?",
                             choices = unique(df$paper_abbrev), 
                             selected = "Celeb. Twitter promo, Indonesia vacc.",
                             multiple = F, width = "300px"),
                 hr(),
                 checkboxInput(inputId = "ToggleMean2",
                               label = "Show aggregated rating",
                               value = FALSE),
                 checkboxInput(inputId = "ToggleRange2",
                               label = "Show aggregated range",
                               value = FALSE),
                 
                 width = 3
               ), fluid = F, position = "right",
               
               # Show the plot with selected info
               mainPanel(
                 plotOutput(outputId = "paperPlot",
                            width = "100%")
               )#/mainPanel
             )#/sideLayout
             
             ),
    
    tabPanel(title = "Journal Ratings",
             
             sidebarLayout(
               sidebarPanel(
                 
                 checkboxGroupInput(
                   inputId = "IncludedPapers2",
                   label = "Which Papers?",
                   choices = unique(df$paper_abbrev),
                   selected = unique(df$paper_abbrev),
                   inline = FALSE,
                   width = "200px",
                   choiceNames = NULL,
                   choiceValues = NULL
                 ),
                 width = 3
               ), fluid = F, position = "right",
               
               # Show the plot with selected info
               mainPanel(
                 plotOutput(outputId = "journalPlot",
                            width = "100%")
               )#/mainPanel
             )#/sideLayout
        ),#/journal ratings
    
    tabPanel(title = "Side-by-side Spider Plots",
             
             fluidRow(
               column(6, 
                      selectInput(inputId = "PaperNameSpider1",
                                  label = "Which paper?",
                                  choices = unique(df$paper_abbrev), 
                                  selected = "Celeb. Twitter promo, Indonesia vacc.",
                                  multiple = F, width = "300px")
                      
                      ),
               column(6,
                      selectInput(inputId = "PaperNameSpider2",
                                  label = "Which paper?",
                                  choices = unique(df$paper_abbrev), 
                                  selected = "Celeb. Twitter promo, Indonesia vacc.",
                                  multiple = F, width = "300px")
                    )
               ),
               
             # Show the plot with selected info
             hr(),
             fluidRow(
               splitLayout(cellWidths = c("50%", "50%"), 
                           plotOutput(outputId = "spiderPlot1"), 
                           plotOutput(outputId = "spiderPlot2")
               )
             )#/fluidrow_plots
             
             ),#/TabPanel
    
    tabPanel(title = "Overlapping Spider Plot",
             
             fluidRow(
               column(9,
                      plotOutput(outputId = "spiderPlotOverlap")
               ),
               column(3, 
                      checkboxGroupInput(
                        inputId = "PaperNameSpiderOverlap",
                        label = "Which Papers?",
                        choices = unique(df$paper_abbrev),
                        selected = unique(df$paper_abbrev)[1:2],
                        inline = FALSE,
                        width = "200px",
                        choiceNames = NULL,
                        choiceValues = NULL
                      )
                      
               )
             )
             
    )#/TabPanel

  )
)

# Define server logic required to draw plot
server <- function(input, output) {

    output$distPlot <- renderPlot({
      
      # set one "set" of dodge width values across layers
      pd = position_dodge(width = 0.8)
      
      if(input$ToggleNonAnonymous){included_evals = df$eval_name[str_starts(df$eval_name, "Anon")]} 
      else {included_evals = df$eval_name} 
      

      # All papers, one rating dot plot ========================================
      p <- df %>% 
        filter(eval_name %in% included_evals) %>% 
        filter(rating_type == input$RatingType) %>% 
        filter(paper_abbrev %in% input$IncludedPapers) %>% 
        filter(!is.na(rating_mean)) %>% 
        mutate(paper_abbrev = fct_reorder(paper_abbrev, rating_mean)) %>% 
        ggplot(aes(x = paper_abbrev, y = est, text = eval_name)) + # dont remove eval name or posdodge stops working (???)
        geom_point(aes(color = paper_color),
                   stat = "identity", size = 2, shape = 18, stroke = 1,
                   position = pd) +
        geom_linerange(aes(ymin = lb_imp, ymax = ub_imp, color = paper_color),
                       position = pd) +
        coord_flip() + # flipping the coordinates to have categories on y-axis (on the left)
        labs(x = "Paper", y = "Rating score",
             title = "Evaluated paper scores") +
        theme_bw() +
        theme(text = element_text(size = 15)) +
        theme(legend.position = "none") +
        scale_x_discrete(labels = function(x) str_wrap(x, width = 20)) +
        scale_color_identity() + # to use paper_color as colors
        ylim(0,100)
      
      if(input$ToggleMean){p = p + geom_point(aes(x = paper_abbrev, y = agg_est), shape = 5, size = 2, stroke = 2, alpha = .1)}
      if(input$ToggleRange){p = p + geom_linerange(aes(ymin = agg_90ci_lb, ymax = agg_90ci_ub), size = 2, alpha = .1)}
      
      p

    }, height = 600, width = 700)
    
    output$paperPlot <- renderPlot({
      
      # set one "set" of dodge width values across layers
      pd = position_dodge(width = 0.8)

      # 1 paper, all ratings dot plot ===================================
      p <- df %>% 
        filter(rating_type != "Merits Journal" & rating_type != "Predicted Journal") %>% 
        mutate(rating_type = fct_drop(rating_type)) %>% #drop unused levels
        filter(paper_abbrev == input$PaperName) %>% 
        ggplot(aes(x = fct_rev(rating_type), y = est, text = eval_name)) + # dont remove eval name or posdodge stops working (???)
        geom_point(aes(color = rating_type),
                   stat = "identity", size = 2, shape = 18, stroke = 1,
                   position = pd) +
        geom_linerange(aes(ymin = lb_imp, ymax = ub_imp, color = rating_type),
                       position = pd) +
        coord_flip() + # flipping the coordinates to have categories on y-axis (on the left)
        labs(x = "Rating Type", y = "Rating score",
             title = "Evaluated paper scores") +
        theme_bw() +
        theme(text = element_text(size = 15)) +
        theme(legend.position = "none") +
        scale_x_discrete(labels = function(x) str_wrap(x, width = 20)) +
        ylim(0,100)
      
      if(input$ToggleMean2){p = p + geom_point(aes(x = fct_rev(rating_type), y = agg_est), shape = 5, size = 2, stroke = 2, alpha = .1)}
      if(input$ToggleRange2){p = p + geom_linerange(aes(ymin = agg_90ci_lb, ymax = agg_90ci_ub), size = 2, alpha = .1)}
      
      p
      
    }, height = 600, width = 700)
    
    output$journalPlot <- renderPlot({
      
      # set one "set" of dodge width values across layers
      pd = position_dodge(width = 0.8)
      
      # All papers, journal information ========================================
      df %>% 
        filter(rating_type %in% c("Merits Journal", "Predicted Journal")) %>% 
        filter(paper_abbrev %in% input$IncludedPapers2) %>% 
        filter(!is.na(rating_mean)) %>% 
        mutate(paper_abbrev = fct_reorder(paper_abbrev, rating_mean)) %>% 
        select(paper_abbrev, eval_name, rating_type, est, paper_color) %>% 
        pivot_wider(names_from = rating_type, values_from = est) %>%
        ggplot(aes(x = paper_abbrev, text = eval_name)) + # dont remove eval name or posdodge stops working (???)
        geom_point(aes(y = `Merits Journal`, color = paper_color, shape = "Merits Journal"),
                   stat = "identity", size = 2, stroke = 2,
                   position = pd) +
        geom_point(aes(y = `Predicted Journal`, color = paper_color, shape = "Predicted Journal"),
                   stat = "identity", size = 2, stroke = 2,
                   position = pd) +
        geom_linerange(aes(ymin = `Merits Journal`, ymax = `Predicted Journal`, color = paper_color), position = pd) +
        coord_flip() + # flipping the coordinates to have categories on y-axis (on the left)
        labs(x = "Paper", y = "Journal tier",
             title = "Merited and predicted journals",
             shape = "Rating") +
        theme_bw() +
        theme(text = element_text(size = 15)) +
        theme(legend.position = "bottom") +
        scale_x_discrete(labels = function(x) str_wrap(x, width = 20)) +
        scale_color_identity() + # to use paper_color as colors
        scale_shape_manual(values = c("Merits Journal" = 3, "Predicted Journal" = 4)) +
        ylim(1,5)
      
    }, height = 600, width = 700)
    
    output$spiderPlot1 <- renderPlot({
      par(mar = c(3, 0.5, 2, 0.5))
      
      
      df %>% 
        select(paper_abbrev, eval_name, rating_type, est) %>%
        filter(rating_type != "Merits Journal" & rating_type != "Predicted Journal") %>% 
        mutate(rating_short = case_match(rating_type,
                                         "Overall assessment" ~ "Overall",
                                         "Methods: justification, reasonableness, validity, robustness" ~ "Methods",
                                         "Engages with real-world, impact quantification" ~ "Real World",
                                         "Advances our knowledge & practice" ~ "Advances Knowledge",
                                         "Logic and communication" ~ "Logic & Communication",
                                         "Relevance to global priorities" ~ "Global Relevance",
                                         "Open, collaborative, replicable science and methods" ~ "Open Science")) %>% 
        pivot_wider(id_cols = c(paper_abbrev, eval_name), names_from = rating_short, values_from = est) %>% 
        filter(paper_abbrev == input$PaperNameSpider1) %>%
        select(-paper_abbrev) %>% 
        column_to_rownames("eval_name") -> dat_spider
      
      # Set graphic colors
      coul <- brewer.pal(nrow(dat_spider), "Set1")
      colors_border <- coul
      colors_in <- scales::alpha(coul,0.3)
      
      dat_plot <- rbind(rep(100,7), rep(0,7), dat_spider)
      
      radarchart(dat_plot, axistype=0, 
                 #custom polygon
                 pcol=colors_border , pfcol=colors_in , plwd=4 , plty=1,
                 #custom the grid
                 cglcol="grey", cglty=2, axislabcol="grey", cglwd=0.8,
                 
      )
      
      legend(x=1.1, y=-0.5, legend = rownames(dat_plot[-c(1,2),]), pch=19, col=colors_in , text.col = "grey20", cex=0.9, pt.cex=2)
      
      
    })
    
    output$spiderPlot2 <- renderPlot({
      par(mar = c(3, 0.5, 2, 0.5))
      
      
      df %>% 
        select(paper_abbrev, eval_name, rating_type, est) %>%
        filter(rating_type != "Merits Journal" & rating_type != "Predicted Journal") %>% 
        mutate(rating_short = case_match(rating_type,
                                         "Overall assessment" ~ "Overall",
                                         "Methods: justification, reasonableness, validity, robustness" ~ "Methods",
                                         "Engages with real-world, impact quantification" ~ "Real World",
                                         "Advances our knowledge & practice" ~ "Advances Knowledge",
                                         "Logic and communication" ~ "Logic & Communication",
                                         "Relevance to global priorities" ~ "Global Relevance",
                                         "Open, collaborative, replicable science and methods" ~ "Open Science")) %>% 
        pivot_wider(id_cols = c(paper_abbrev, eval_name), names_from = rating_short, values_from = est) %>% 
        filter(paper_abbrev == input$PaperNameSpider2) %>%
        select(-paper_abbrev) %>% 
        column_to_rownames("eval_name") -> dat_spider
      
      # Set graphic colors
      coul <- brewer.pal(nrow(dat_spider), "Set1")
      colors_border <- coul
      colors_in <- scales::alpha(coul,0.3)
      
      dat_plot <- rbind(rep(100,7), rep(0,7), dat_spider)
      
      
      
      radarchart(dat_plot, axistype=0, 
                 #custom polygon
                 pcol=colors_border , pfcol=colors_in , plwd=4 , plty=1,
                 #custom the grid
                 cglcol="grey", cglty=2, axislabcol="grey", cglwd=0.8,
                 
      )
      
      legend(x=1.1, y=-0.5, legend = rownames(dat_plot[-c(1,2),]), pch=19, col=colors_in , text.col = "grey20", cex=0.9, pt.cex=2)
      
      
    })

    output$spiderPlotOverlap <- renderPlot({
      par(mar = c(5, 1, 1, 15),
          xpd = TRUE)
      
      
      df %>% 
        select(paper_abbrev, rating_type, rating_mean) %>%
        filter(paper_abbrev %in% input$PaperNameSpiderOverlap) %>%
        filter(rating_type != "Merits Journal" & rating_type != "Predicted Journal") %>% 
        mutate(rating_short = case_match(rating_type,
                                         "Overall assessment" ~ "Overall",
                                         "Methods: justification, reasonableness, validity, robustness" ~ "Methods",
                                         "Engages with real-world, impact quantification" ~ "Real World",
                                         "Advances our knowledge & practice" ~ "Advances Knowledge",
                                         "Logic and communication" ~ "Logic & Communication",
                                         "Relevance to global priorities" ~ "Global Relevance",
                                         "Open, collaborative, replicable science and methods" ~ "Open Science")) %>% 
        distinct() %>% 
        pivot_wider(id_cols = c(paper_abbrev), names_from = rating_short, values_from = rating_mean) %>% 
        column_to_rownames("paper_abbrev") -> dat_spider
      
      # Set graphic colors
      coul <- brewer.pal(nrow(dat_spider), "Set1")
      colors_border <- coul
      colors_in <- scales::alpha(coul,0.3)
      
      dat_plot <- rbind(rep(100,7), rep(0,7), dat_spider)
      
      radarchart(dat_plot, axistype=0, 
                 #custom polygon
                 pcol=colors_border , pfcol=colors_in , plwd=4 , plty=1,
                 #custom the grid
                 cglcol="grey", cglty=2, axislabcol="grey", cglwd=0.8,
                 
      )
      
      legend(x=1.8, y=0,
             legend = rownames(dat_plot[-c(1,2),]), 
             pch=19, col=colors_in , text.col = "grey20", cex=0.9, pt.cex=2)
      
      
    })
    
    
    
}

# Run the application 
shinyApp(ui = ui, server = server)
