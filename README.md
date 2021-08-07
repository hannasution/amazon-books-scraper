<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- ABOUT THE PROJECT -->
## About The Project

Scraping Amazon bestseller books for all category in it using scrapy python. Story: I was very bored, then thought about this project that has not been touched for a long time, so I thought to modify and improve from the old project. the purpose of this project is to hone my scraping skills using python.


### Built With

* [Scrapy](https://scrapy.org/)
* [Python](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:hannasution/amazon-books-scraper.git
   ```



<!-- USAGE EXAMPLES -->
## Usage

To run scraping book use this command:
```command
   scrapy crawl book
   ```
if you want to save the result run this command:
```command
   scrapy crawl book -o books.json
   ```

For more usage, please refer to the [Scrapy Documentation](https://scrapy.org/doc/)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
