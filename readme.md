<!-- markdownlint-disable MD033 MD041 MD007 -->

<!-- pretty badges -->
<div align="center">
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Language Badge"/>
  <img src="https://img.shields.io/badge/Version-0.1.0-blue" alt="Version Badge">
  <img src="https://img.shields.io/badge/License-MIT-dark_green.svg" alt="License Badge"/>
  <img src="https://img.shields.io/badge/School-ULB-yellow" alt="School Badge"/>
</div>

# 🔎 Bloom Filter

Welcome to my **Bloom Filter** project ! This project is part of the **Randomized Algorithms INFO—F413** at `ULB`. It implements a **Bloom filter** along with a **Hash Factory**, enabling efficient probabilistic membership queries!

<div align="center">
  <img src="res/intro.jpg" alt="bloom filter" width="400"/>
</div>

## 📜 Description

This Python project provides:

- A **Bloom filter** data structure capable of storing integers **efficiently**.
- A **Hash Factory** for generating independent **universal hash functions**.
- Methods to **add** elements and **check membership** with probabilistic guarantees.

For more detailed problem specifications and additional information, please refer to the project specification [**`doc/BloomAssignment.pdf`**](doc/BloomAssignment.pdf) or to the report [**`doc/infof413_report.pdf`**](doc/infof413_report.pdf).

## ⚙️ Installation

1. Clone the repository:

    ```sh
    git clone git@github.com:Ant0in/BloomFilter.git
    cd BloomFilter
    ```

2. Make sure you have **Python 3.10+** installed with **`pip`**. Then install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. **(Optional)** To keep the environment isolated, you can create and activate a `virtual environment`:

    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

This ensures all packages are contained *locally* and avoids conflicts with system-wide Python packages.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgements

This project was developed for the **`Randomized algorithms`** course **`INFO—F413`**. Special thanks to **`Jean Cardinal (ULB)`** for their guidance and support.
