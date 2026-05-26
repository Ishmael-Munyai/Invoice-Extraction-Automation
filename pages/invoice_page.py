from playwright.sync_api import sync_playwright
import os

class InvoicePage:
  def __init__(self, page):
    self.page = page

  def download_invoices(self):
    # Locate all table rows (adjust selector to your table)
    rows = self.page.query_selector_all("table#invoiceTable tbody tr")

    for idx, row in enumerate(rows):
      print(f"Processing row {idx}")

      # Click the download link/button inside the row
      download_link = row.query_selector("a.download")
      if download_link:
        download = self.page.expect_download()
        download_link.click()
        path = self.download.path()
        save_path = os.path.join(self.download_dir, download.suggested_filename)
        self.download.save_as(save_path)
        print(f"Downloaded: {save_path}")

        # Extract invoice details
        self.extract_invoice_data(save_path)

            #browser.close()