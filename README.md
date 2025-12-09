# Taurus Space: Secure Logistics Platform (Sanitized Case Study)

> **Context:** This repository serves as a functional work sample for the **Technical Program Manager** application at **8090**.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]
(https://8090-case-study.streamlit.app/)

## 🎯 The Objective
At **8090**, the goal is to dismantle the "Software Industrial Complex" by building efficient, purpose-built software factories.

I created this interactive application to demonstrate that philosophy in action. Rather than sending a static PDF or a slide deck, I built a live, "low-code" artifact that demonstrates how I managed the delivery of a complex **Deep Tech** product serving both **Commercial** and **U.S. Defense** sectors.

## 🛠 What This App Demonstrates
1.  **Requirement Translation:** How I bridged the gap between ambiguous "Dual-Use" requirements and a concrete technical architecture.
2.  **Architecture as Code:** Using `Graphviz` to dynamically visualize the modular system design that enabled code reuse across security domains.
3.  **Governance & Metrics:** A breakdown of the KPIs used to measure delivery velocity and security compliance.

## 🏗 Architecture Strategy (The "Software Factory" Approach)
The core challenge at Taurus Space was delivering one product to two diametrically opposed environments:
* **Commercial:** Public Cloud, Rapid CI/CD, Open APIs.
* **Defense:** Air-Gapped, Rigid Security Gates (IL-5), Static Binaries.

**The Solution:** A unified pipeline that forks at the build stage, maximizing code reuse (85%) while satisfying strict compliance constraints.

## 🚀 Quick Start (Run Locally)
If you prefer to run this artifact locally rather than viewing the deployed version:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/nioshak/taurus-case-study.git](https://github.com/nioshak/taurus-case-study.git)
    cd taurus-case-study
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

## 🧰 Tech Stack
* **Framework:** Streamlit (Python) - *Chosen for rapid prototyping and interactive data visualization.*
* **Visualization:** Graphviz - *Chosen to render architecture diagrams dynamically.*
* **Deployment:** Streamlit Cloud via GitHub Actions.

---

**Author:** Niosha Kayhani

https://linkedin.com/in/niosha-kayhani
