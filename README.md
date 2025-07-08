<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project\_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/Grizmo2610/CVScanner">
    <img src="static/images/Logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">CV AI Summarizer</h3>

  <p align="center">
    Scan, summarize, and check if your resume matches the job description
    <br />
    <a href="https://github.com/Grizmo2610/CVScanner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://cv-ai-summarizer.onrender.com/">View Demo</a>
    &middot;
    <a href="https://github.com/Grizmo2610/CVScanner/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Grizmo2610/CVScanner/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![Product-Screenshot](static/images/product-screenshot.png)

Nowadays, creating a personal resume (CV) is easier than ever. However, due to the overwhelming number of candidates following popular templates and trends, recruiters often face the burden of reading through a flood of CVs to find suitable matches. At the same time, applicants themselves may want to know how well their CV aligns with a given job description.

This tool helps bridge that gap and save time for both parties—employers and candidates—by leveraging artificial intelligence to analyze resumes. It extracts and summarizes candidate information (optional), compares it against job descriptions, and then evaluates the match percentage between the JD and the CV.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)](https://www.python.org/)
* [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)](https://flask.palletsprojects.com/)
* [![LLM](https://img.shields.io/badge/LLM-Large%20Language%20Model-blueviolet?style=for-the-badge)](https://en.wikipedia.org/wiki/Large_language_model)
* [![PyMuPDF](https://img.shields.io/badge/PyMuPDF-PDF%20Parser%20%26%20Renderer-green?style=for-the-badge)](https://pymupdf.readthedocs.io/)
* [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Getting started with the app is easy. If you just want to use it, I recommend accessing the demo version via this link: [AI CV Summarizer](https://cv-ai-summarizer.onrender.com/).

However, if you want to modify or upgrade the source code to suit your needs (which I totally encourage), or simply want to run it locally on your own system, follow the guide below.

### Prerequisites

* Python 3.11 or higher
* pip installed
* Basic knowledge of Python

### Installation

Below are the installation steps. These are written from a Windows perspective, but the steps can be adapted to macOS/Linux easily.

1. First, clone this repository:

```bash
git clone https://github.com/Grizmo2610/CVScanner.git
cd CVScanner
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

> `venv` is the name of the virtual environment—you can change it if you'd like.

3. Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

4. Get a free Google API Key at [https://developers.google.com/maps/documentation/javascript/get-api-key](https://developers.google.com/maps/documentation/javascript/get-api-key)

5. Create a `gemini.key` file and paste the path to this file into the `gemini_key_path` variable in [app.py](app.py).

6. Inside the `gemini.key` file, paste your API key (from step 4). **Do not include any comments or extra characters**.

7. Run the app:

```bash
python app.py
```

8. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the app.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

You need to upload your resume file first. Then, customize the following settings:

* `Output Language`: Language of the CV summary (default: Vietnamese)
* `Summary Length`: Length of the summary (default: 500 words)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* [x] Read CV
  * [x] PDF
  * [ ] DOCX
  * [ ] Image
* [x] Extract information and summarize content
* [x] Build a basic web interface and demo
  * [x] Web interface with HTML and CSS
  * [x] Use Flask backend to read and process data
* [x] Return results with highlight
* [x] Set up repositories
* [ ] Add JD analysis and comparison features
  * [ ] Add a section to input JD
    * [ ] Manual input
    * [ ] Upload file
  * Add JD analysis
* [ ] Compare JD with CV


See the [open issues](https://github.com/Grizmo2610/CVScanner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/Grizmo2610/CVScanner/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Grizmo2610/CVScanner" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Hoàng Tuấn Tú (You can call me as Grizmo) - [@grizmo](https://www.linkedin.com/in/grizmo/) - hoangtuantu893@gmail.com

Project Link: [https://github.com/Grizmo2610/CVScanner](https://github.com/Grizmo2610/CVScanner)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [othneildrew README Template](https://github.com/othneildrew/Best-README-Template)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Choose an Open Source License](https://choosealicense.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Grizmo2610/CVScanner.svg?style=for-the-badge
[contributors-url]: https://github.com/Grizmo2610/CVScanner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Grizmo2610/CVScanner.svg?style=for-the-badge
[forks-url]: https://github.com/Grizmo2610/CVScanner/network/members
[stars-shield]: https://img.shields.io/github/stars/Grizmo2610/CVScanner.svg?style=for-the-badge
[stars-url]: https://github.com/Grizmo2610/CVScanner/stargazers
[issues-shield]: https://img.shields.io/github/issues/Grizmo2610/CVScanner.svg?style=for-the-badge
[issues-url]: https://github.com/Grizmo2610/CVScanner/issues
[license-shield]: https://img.shields.io/github/license/Grizmo2610/CVScanner.svg?style=for-the-badge
[license-url]: https://github.com/Grizmo2610/CVScanner/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/grizmo
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 