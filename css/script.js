// Mobile Navigation Toggle
document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.querySelector(".hamburger")
  const navMenu = document.querySelector(".nav-menu")
  const socialLinks = document.querySelector(".social-links")

  if (hamburger) {
    hamburger.addEventListener("click", () => {
      const isExpanded = hamburger.getAttribute("aria-expanded") === "true"
      
      hamburger.classList.toggle("active")
      navMenu.classList.toggle("active")
      socialLinks.classList.toggle("active")
      
      // Update aria-expanded for accessibility
      hamburger.setAttribute("aria-expanded", !isExpanded)
    })
  }

  // Close mobile menu when clicking on a link
  const navLinks = document.querySelectorAll(".nav-link")
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("active")
      navMenu.classList.remove("active")
      socialLinks.classList.remove("active")
      
      // Reset aria-expanded when closing menu
      hamburger.setAttribute("aria-expanded", "false")
    })
  })

  // Smooth scrolling for navigation links
  const links = document.querySelectorAll('a[href^="#"]')
  links.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault()
      const targetId = this.getAttribute("href")
      const targetSection = document.querySelector(targetId)

      if (targetSection) {
        const offsetTop = targetSection.offsetTop - 80 // Account for fixed navbar
        window.scrollTo({
          top: offsetTop,
          behavior: "smooth",
        })
      }
    })
  })

  // Add scroll effect to navbar
  window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar")
    if (window.scrollY > 50) {
      navbar.style.background = "rgba(2, 6, 23, 0.98)"
      navbar.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.5)"
    } else {
      navbar.style.background = "rgba(2, 6, 23, 0.85)"
      navbar.style.boxShadow = "none"
    }
  })

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches

  // Typing loop in the hero terminal
  const typedEl = document.getElementById("typed")
  if (typedEl) {
    const cmds = ["ls projets/", "make && ./portfolio", "git push origin main", 'grep -r "passion" .']
    if (reducedMotion) {
      typedEl.textContent = cmds[0]
    } else {
      let i = 0
      let j = 0
      let deleting = false
      const tick = () => {
        const word = cmds[i]
        typedEl.textContent = word.slice(0, j)
        if (!deleting && j < word.length) {
          j++
          setTimeout(tick, 70)
        } else if (!deleting) {
          deleting = true
          setTimeout(tick, 1800)
        } else if (j > 0) {
          j--
          setTimeout(tick, 35)
        } else {
          deleting = false
          i = (i + 1) % cmds.length
          setTimeout(tick, 400)
        }
      }
      tick()
    }
  }

  // Scroll reveal for cards and badges
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible")
        observer.unobserve(entry.target)
      }
    })
  }, { threshold: 0.12, rootMargin: "0px 0px -50px 0px" })

  const animatedElements = document.querySelectorAll(
    ".about-card, .experience-card, .project-card, .achievement-item, .skills-marquee"
  )
  animatedElements.forEach((el) => {
    if (!reducedMotion) {
      el.classList.add("reveal")
    }
    observer.observe(el)
  })
})

// Add mobile navigation styles
const style = document.createElement("style")
style.textContent = `
    @media (max-width: 768px) {
        .nav-menu.active,
        .social-links.active {
            display: flex;
            position: absolute;
            top: 100%;
            left: 0;
            width: 100%;
            background: #020617;
            flex-direction: column;
            padding: 1rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
        }

        .nav-menu.active {
            border-bottom: 1px solid #334155;
        }
        
        .social-links.active {
            justify-content: center;
            padding: 1rem;
        }
        
        .hamburger.active span:nth-child(1) {
            transform: rotate(-45deg) translate(-5px, 6px);
        }
        
        .hamburger.active span:nth-child(2) {
            opacity: 0;
        }
        
        .hamburger.active span:nth-child(3) {
            transform: rotate(45deg) translate(-5px, -6px);
        }
    }
`
document.head.appendChild(style)
