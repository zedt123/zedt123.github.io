import os
import glob
from datetime import datetime

def generate_sitemap(site_url, site_dir):
    """
    site_url: The base URL of your site, e.g. 'https://example.com'
    site_dir: The directory where Quarto outputs HTML files, e.g. '_site'
    """
    # Find all HTML files in site_dir
    html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)
    
    # Start building the sitemap string (XML format)
    sitemap_entries = []
    sitemap_entries.append('<?xml version="1.0" encoding="UTF-8"?>')
    sitemap_entries.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for html_file in html_files:
        # Convert local file path to a URL path
        rel_path = os.path.relpath(html_file, site_dir)
        # If your site uses clean URLs, you might drop '.html' from the URL. Otherwise keep as is.
        # We'll keep .html for simplicity:
        page_url = f"{site_url}/{rel_path.replace(os.sep, '/')}"
        
        # You might also set a <lastmod> based on the file’s modification time
        lastmod = datetime.utcfromtimestamp(os.path.getmtime(html_file)).strftime('%Y-%m-%d')
        
        entry = f"""
  <url>
    <loc>{page_url}</loc>
    <lastmod>{lastmod}</lastmod>
  </url>
"""
        sitemap_entries.append(entry.strip())
    
    sitemap_entries.append('</urlset>')
    
    return "\n".join(sitemap_entries)

def main():
    site_url = "https://zedt123.github.io"  # <-- Replace with your actual production site URL
    site_dir = "docs"                # <-- The default Quarto output directory
    
    sitemap_xml = generate_sitemap(site_url, site_dir)
    
    # Write sitemap.xml into the _site directory
    with open(os.path.join(site_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

if __name__ == "__main__":
    main()
