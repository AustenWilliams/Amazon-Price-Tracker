# Amazon-Price-Tracker
> Amazon price checker that compares past values with current price values.
> Can only get to work on macOS due to database issues using "Shelve" module. I am working on changing the database used.

Begginer Python 3 project that utilizes Tkinter and Selenium Webdriver to check for prices of a specific product and determine if the price has gone up or down.

![](https://github.com/AustenWilliams/Amazon-Price-Tracker/blob/master/Wiki/Description.png)
![](https://github.com/AustenWilliams/Amazon-Price-Tracker/blob/master/Wiki/gui.png)


## Installation Instructions

To use this software you must first install [Selenium][Selenium]. This can be done very easily using the pip installer for Python. Simply open your terminal or command line and enter:
```
pip install selenium 
```

In addition, I have provided the [chromedriver] used to navigate the Chrome web browser in the background also known as the headless browser. Since this uses a chromedriver it will only work on chrome browsers. You can check out the documentation for both in their respective hyperlinks.


## Usage example

_For more examples and usage, please refer to the [Wiki][wiki]._

## Contact

Austen Williams  – Austen_Will@yahoo.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/AustenWilliams](https://github.com/AustenWilliams)

## Contributing

1. Fork it (<https://github.com/AustenWilliams/Amazon-Price-Tracker.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/AustenWilliams/Amazon-Price-Tracker/wiki
[Selenium]: https://selenium.dev/documentation/en/
[chromedriver]: https://chromedriver.chromium.org
