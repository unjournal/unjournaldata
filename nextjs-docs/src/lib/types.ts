export interface PageData {
  slug: string;
  content: string;
  pageId: string;
  lastFetched?: Date;
}

export interface PageParams {
  params: Promise<{
    slug: string;
  }>;
}

export interface ExportInitResponse {
  id: string;
  status: 'inProgress' | 'complete' | 'failed';
  href: string;
  downloadLink?: string;
}
