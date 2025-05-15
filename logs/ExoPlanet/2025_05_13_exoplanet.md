# 🌌 ExoPlanet Dev Log - Day 1
**Date:** 2025-05-13  
**Focus:** Foundation build of GalaxyMap and StarSystem scene transitions  
**Goal:** Clean, incremental build of a working star-click → system view loop

---

## ✅ What Was Built

### 🔭 Scene 1: `GalaxyMap`
- Procedural generation of 10 clickable stars using `StarSpawner.cs`
- Each star is a circle prefab with:
  - Unique name (`Star 0` to `Star 9`)
  - Unique ID
  - `CircleCollider2D` for click detection
- `StarInfo.cs` detects click and:
  - Logs ID + name
  - Passes info to `GameManager`
  - Loads `StarSystem` scene

### 🧠 Global State: `GameManager.cs`
- Singleton pattern (persists across scenes)
- Stores:
  - `currentStarID`
  - `currentStarName`

---

## 🪐 Scene 2: `StarSystem`
- Scene created and added to Build Settings
- Reads current star name from `GameManager`
- Displays it using **TextMeshPro UI**:
  - Top-centered, fully anchored and responsive
- Instantiates a copy of the clicked star prefab in the center of the system

---

## 📘 Key Unity Concepts Used

| Concept | Notes |
|--------|-------|
| Singleton | GameManager pattern for cross-scene data |
| SceneManager | Handles scene switching from code |
| Prefabs | Reusable star objects generated at runtime |
| Random.insideUnitCircle | Positions stars within a circular galaxy layout |
| TextMeshPro | For modern, high-quality UI text |
| Anchors + Pivot | Crucial for dynamic screen positioning (top-center used) |
| Collider2D + OnMouseDown | Used for star click detection in 2D world |

---

## 🔄 Working Loop Confirmed

- ✅ Stars populate and can be clicked
- ✅ Clicking a star passes info and loads new scene
- ✅ System name shows at top of new scene
- ✅ Star is visualized again in center of the system

---

## 🧠 Review & Learning Goals

- [ ] Review `Singleton` vs other data persistence approaches
- [ ] Understand scene build settings and Build Profiles (Unity 6)
- [ ] Practice canvas anchoring and UI layout in TextMeshPro
- [ ] Test adding dynamic content (e.g., planets) to `StarSystem`

---

## ⏭️ Next Steps

1. Add **Back to Galaxy** button to return to `GalaxyMap`
2. Generate **placeholder planets** in orbit (e.g., circles around center star)
3. Begin **planet interaction** (info panel, colonization button)
4. Add tick-based **resource system**

---

## 🧠 George AI Prompt for Tomorrow

> "Summarize the GalaxyMap → StarSystem scene flow. What data is passed, and how is it used? What part of the project needs the most UI anchoring care?"

---

