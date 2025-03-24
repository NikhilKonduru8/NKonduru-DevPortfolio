# Insight HQ - Hackathon Project

This repository contains the HTML and CSS for "Insight HQ," a website developed as a hackathon project. Insight HQ is a concept for a business intelligence platform aimed at transforming data into actionable insights for business leaders.

## Project Overview

Insight HQ was created during a hackathon to address the challenge of making business data more accessible and actionable. The website showcases the core features of this platform, including real-time analytics, customer feedback analysis, and partner matching, through a modern and user-friendly interface.

## Key Features (Conceptual)

-   **Real-Time Analytics:** Demonstrates how key performance metrics could be tracked via customizable dashboards.
-   **Customer Feedback Analysis:** Illustrates the potential for gathering and analyzing customer reviews to drive improvements.
-   **Partner Matching:** Showcases the concept of discovering relevant sponsors and partners.
-   **Responsive Design:** Ensures the website concept is adaptable to various screen sizes, crucial for modern web applications.
-   **Modern UI with Animations:** Uses a clean, engaging design with CSS animations to enhance the user experience.
-   **Custom Cursor:** Includes an interactive cursor for a more engaging feel.

## Technologies Used

-   **HTML:** For the website's structure and content.
-   **CSS:** For styling and layout, including custom properties for easy theme management.
-   **Font Awesome:** For icons to enhance visual communication.

## File Structure

-   `index.html`: The main HTML file containing the website's structure.
-   `style.css`: The CSS file containing all styling rules.
-   `graph.png`: An example image used in the analytics preview.
-   `nikhi.jpg`, `arni.jpg`, `lalu.jpg`, `adi.jpg`: Images of the hackathon team members.

## CSS Custom Properties (Variables)

The CSS utilizes custom properties to streamline color management and theming:

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
