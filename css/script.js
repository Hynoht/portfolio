document.addEventListener("DOMContentLoaded", () => {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches

  const toggle = document.querySelector(".nav-toggle")
  const nav = document.getElementById("site-nav")
  if (toggle && nav) {
    const label = toggle.querySelector(".visually-hidden")
    const setOpen = (open) => {
      nav.classList.toggle("is-open", open)
      toggle.setAttribute("aria-expanded", String(open))
      label.textContent = open ? toggle.dataset.labelClose : toggle.dataset.labelOpen
    }
    toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"))
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        setOpen(false)
        toggle.focus()
      }
    })
    document.addEventListener("click", (e) => {
      if (nav.classList.contains("is-open") && !nav.contains(e.target) && !toggle.contains(e.target)) setOpen(false)
    })
  }

  const header = document.querySelector(".site-header")
  if (header) {
    const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 8)
    onScroll()
    window.addEventListener("scroll", onScroll, { passive: true })
  }

  if (!reducedMotion && "IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible")
          observer.unobserve(entry.target)
        }
      })
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" })

    document.querySelectorAll(".reveal-item").forEach((el) => {
      if (el.getBoundingClientRect().top > window.innerHeight) {
        el.classList.add("reveal")
        observer.observe(el)
      }
    })
  }

  const filters = document.querySelector(".filters")
  const grid = document.querySelector("[data-filter-grid]")
  if (filters && grid) {
    const buttons = filters.querySelectorAll(".filter")
    const cards = grid.querySelectorAll("[data-cat]")
    const status = document.querySelector("[data-filter-status]")
    const lang = document.documentElement.lang
    filters.hidden = false
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const cat = btn.dataset.filter
        buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)))
        let shown = 0
        cards.forEach((card) => {
          const match = cat === "all" || card.dataset.cat === cat
          card.hidden = !match
          if (match) {
            shown++
            card.classList.remove("reveal")
          }
        })
        if (status) status.textContent = lang === "fr" ? `${shown} projet(s) affiché(s)` : `${shown} project(s) shown`
      })
    })
  }
})
