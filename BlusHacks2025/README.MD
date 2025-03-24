# Insight HQ - Business Intelligence Platform

This repository contains the HTML and CSS for a website showcasing "Insight HQ," a business intelligence platform designed to transform data into actionable insights.

## Overview

Insight HQ is presented as a comprehensive tool for business leaders, offering real-time analytics, customer feedback analysis, and partner matching. The website aims to highlight these features through a clean, modern design with a focus on user experience.

## Features

-   **Real-Time Analytics:** Track key performance metrics with customizable dashboards.
-   **Customer Feedback Analysis:** Gather and analyze customer reviews to improve products and services.
-   **Partner Matching:** Discover potential sponsors and partners aligned with your business goals.
-   **Responsive Design:** Ensures the website looks great on various devices.
-   **Modern UI:** Utilizes a clean, intuitive design with subtle animations for enhanced user engagement.
-   **Custom Cursor:** A unique interactive cursor for better user experience.

## Technologies Used

-   **HTML:** For structuring the website content.
-   **CSS:** For styling and layout, including custom properties for easy color management.
-   **Font Awesome:** For icons.

## File Structure

-   `index.html`: The main HTML file containing the website structure.
-   `style.css`: The CSS file containing all the styling rules.
-   `graph.png`: An image used for the analytics preview.
-   `nikhi.jpg`, `arni.jpg`, `lalu.jpg`, `adi.jpg`: Images of the developers.

## CSS Custom Properties

The CSS uses custom properties (CSS variables) for easy color and style management:

```css
:root {
    --beige: #f5f5dc;
    --beige-light: #faf9f0;
    --charcoal: #36454f;
    --charcoal-light: #4a5c68;
    --black: #000000;
    --navy: #4a6baf;
    --navy-light: #7289c7;
    --navy-dark: #3a5495;
    --white: #ffffff;
    --light-gray: #f9f9f9;
    --border-color: #eaeaea;
    --shadow-color: rgba(0, 0, 0, 0.08);
    --shadow-dark: rgba(0, 0, 0, 0.15);
    --transition-speed: 0.3s;
    --transition-speed-slow: 0.5s;
    --gradient-primary: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
    --gradient-dark: linear-gradient(135deg, var(--charcoal) 0%, var(--charcoal-light) 100%);
}
