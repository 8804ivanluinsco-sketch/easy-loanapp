window.tailwind = window.tailwind || {};
window.tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "on-secondary-fixed-variant": "#364b40",
        "tertiary-fixed-dim": "#a7ccdf",
        "surface-tint": "#006a6a",
        "on-secondary": "#ffffff",
        "surface-dim": "#d7dbda",
        "secondary-fixed": "#d0e8d9",
        "primary-fixed-dim": "#84d4d3",
        "on-tertiary-fixed-variant": "#264b5b",
        "outline-variant": "#bec9c8",
        "surface-bright": "#f7faf9",
        "inverse-primary": "#84d4d3",
        "surface-container": "#ebeeee",
        "on-secondary-container": "#51685b",
        "secondary": "#4d6357",
        "secondary-container": "#cde6d6",
        "background": "#f7faf9",
        "surface-variant": "#e0e3e2",
        "on-error": "#ffffff",
        "inverse-on-surface": "#eef1f0",
        "on-tertiary": "#ffffff",
        "tertiary": "#264b5b",
        "tertiary-container": "#3f6374",
        "secondary-fixed-dim": "#b4ccbd",
        "on-surface": "#181c1c",
        "on-background": "#181c1c",
        "surface": "#f7faf9",
        "surface-container-lowest": "#ffffff",
        "primary-fixed": "#a0f0f0",
        "on-tertiary-fixed": "#001f2a",
        "error-container": "#ffdad6",
        "on-primary": "#ffffff",
        "surface-container-low": "#f1f4f3",
        "on-surface-variant": "#3e4948",
        "on-primary-fixed-variant": "#004f4f",
        "on-primary-container": "#97e7e6",
        "primary": "#005050",
        "surface-container-highest": "#e0e3e2",
        "outline": "#6e7979",
        "error": "#ba1a1a",
        "surface-container-high": "#e6e9e8",
        "on-primary-fixed": "#002020",
        "inverse-surface": "#2d3131",
        "tertiary-fixed": "#c2e8fc",
        "on-tertiary-container": "#b9def2",
        "on-secondary-fixed": "#0a1f16",
        "on-error-container": "#93000a",
        "primary-container": "#006a6a"
      },
      borderRadius: {
        DEFAULT: "0.125rem",
        lg: "0.25rem",
        xl: "0.5rem",
        full: "0.75rem"
      },
      fontFamily: {
        headline: ["Manrope", "sans-serif"],
        body: ["Inter", "sans-serif"],
        label: ["Inter", "sans-serif"]
      }
    }
  }
};

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-icon]").forEach((icon) => {
    if (!icon.textContent.trim()) {
      icon.textContent = icon.dataset.icon;
    }
  });

  const panelLinks = document.querySelectorAll("[data-dashboard-panel-link]");
  const panels = document.querySelectorAll("[data-dashboard-panel]");

  if (panelLinks.length && panels.length) {
    const activatePanel = (panelName, shouldBlink = false) => {
      const targetPanel = document.querySelector(`[data-dashboard-panel="${panelName}"]`);

      if (!targetPanel) {
        return;
      }

      panels.forEach((panel) => {
        panel.classList.toggle("dashboard-panel-hidden", panel.dataset.dashboardPanel !== panelName);
      });

      panelLinks.forEach((link) => {
        link.classList.toggle("active", link.dataset.dashboardPanelLink === panelName);
      });

      if (shouldBlink) {
        targetPanel.classList.remove("dashboard-panel-blink");
        void targetPanel.offsetWidth;
        targetPanel.classList.add("dashboard-panel-blink");
      }
    };

    panelLinks.forEach((link) => {
      link.addEventListener("click", (event) => {
        event.preventDefault();
        activatePanel(link.dataset.dashboardPanelLink, true);
      });
    });

    const openedFromHash = window.location.hash === "#my-loans";
    const initialPanel = openedFromHash ? "my-loans" : "overview";
    activatePanel(initialPanel, openedFromHash);
  }
});
