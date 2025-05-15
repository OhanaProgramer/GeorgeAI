# 🌌 ExoPlanet Dev Log - Day 2
**Date:** 2025-05-15  
**Focus:** Planet generation, visual polish, full scene loop

---

## ✅ What Was Built

### 🚀 Star System Scene Now Includes:
- Center star prefab (visually shown)
- Planets A–D placed around the star in circular formation
- TextMeshPro label showing system name
- Responsive back button

---

## 🧠 Core Concepts Used

| Concept | Description |
|--------|--------------|
| Circular Math | Used `Mathf.Cos/Sin(angle) * radius` to space planets |
| Prefab Instancing | Planets created at runtime, named by ID |
| Singleton Data Sharing | Star name passed via `GameManager` |
| Scene Navigation | Full loop with `SceneManager.LoadScene()` |
| UI Canvas Scaling | Fixed anchor/pivot alignment for portable UI |

---

## 🧪 Testing Notes

- Confirmed 4 planets spawn per system
- Each has unique name (A, B, C, D)
- Scene loop is clean and consistent
- Camera shows all elements clearly on any screen size

---

## 📌 Next Sprint Options (Day 3)

- [ ] Add `PlanetInfo` script to handle clicks
- [ ] UI popup or side panel to show planet details
- [ ] Add fake colonization data (resource %, habitable yes/no)
- [ ] Begin mock colonize action → log to Console

---

## 🧠 George AI Prompt for Tomorrow

> "How can I begin to track which planets are colonized and which systems have been visited? What’s the lightest-weight way to do this in Unity?"

