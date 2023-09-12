# Unjournal Data Dashboard
# By Julia Bottesini
#

library(shiny)
library(tidyverse)
library(RColorBrewer)

# Import data
df <- read_rds("shiny_explorer.rds")

# create a palette with a color for each paper
color_count = df$paper_abbrev %>% unique() %>% length()
#my_pal = distinctColorPalette(color_count)
my_pal = colorRampPalette(brewer.pal(8, "Set1"))(color_count)


# create new variables
df <- df %>% 
  group_by(paper_abbrev, rating_type) %>% 
  mutate(n_evals = n(), # number of evaluators for each paper
         rating_mean = mean(est, na.rm = T)) %>%  # replace with aggreCAT functions later
  ungroup() %>%
  nest(.by = paper_abbrev) %>% 
  mutate(paper_color = my_pal) %>% # give each paper its own color
  unnest(cols = c(data))

# categories
rating_cats <- c("overall", "adv_knowledge", "methods", "logic_comms", "real_world", "gp_relevance", "open_sci")
pred_cats <- c("journal_predict", "merits_journal")

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Unjournal Evaluation Data"),

    # Sidebar with plot options
    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "RatingType",
                        label = "Rating Type:",
                        choices = c(rating_cats, pred_cats), 
                        selected = "overall",
                        multiple = F),
            
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
        )
    )
)

# Define server logic required to draw plot
server <- function(input, output) {

    output$distPlot <- renderPlot({
      
      # set one "set" of dodge width values across layers
      pd = position_dodge(width = 0.8)
      

      # Dot plot
      df %>% 
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
        geom_point(aes(x = paper_abbrev, y = rating_mean),
                       shape = 5, size = 2, stroke = 2) +
        coord_flip() + # flipping the coordinates to have categories on y-axis (on the left)
        labs(x = "Paper", y = "Rating score",
             title = "Scores of evaluated papers") +
        theme_bw() +
        theme(text = element_text(size = 15)) +
        theme(legend.position = "none") +
        scale_x_discrete(labels = function(x) str_wrap(x, width = 20)) +
        scale_color_identity() # to use paper_color as colors

    }, height = 600, width = 700)
}

# Run the application 
shinyApp(ui = ui, server = server)
