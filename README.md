

# 📈 PolarGraph.py

**PolarGraph.py** is an interactive Python script that generates and saves graphs of polar functions for use in test documents, LaTeX templates, or presentations.

---

## 🔹 Features

- Enter a polar function \( r(\theta) \) interactively.
- Customize the θ range and number of sampling points.
- Automatically save clean, high-DPI (300 dpi) images.
- Standardized 6×6 inch figures for easy LaTeX and exam insertion.
- Polar axis labels are neatly shown in multiples of \( \pi/12 \).
- Light-gray grid and tick marks for clean presentation.

---

## 🔹 Requirements

You need Python 3 and the following libraries installed:
- `numpy`
- `matplotlib`

If you're using a virtual environment (recommended), you can install them with:

```bash
uv pip install numpy matplotlib
```

or

```bash
pip install numpy matplotlib
```

---

## 🔹 How to Run

From the command line, inside your project folder:

```bash
python PolarGraph.py
```

---

## 🔹 Usage Instructions

You will be prompted for:

1. **Polar function** (in terms of `theta`):  
   Examples:
   - `3*sin(2*theta)`
   - `1 + 2*cos(5*theta)`
   - `2`
   - `theta**2`
   
   **Note:** Only `theta` is allowed as the variable. Common math functions like `sin`, `cos`, `sqrt`, and constants like `pi` and `e` are available.

2. **θ Range (start,end in radians)**:  
   - Leave blank for the default `[0, 2π]`.
   - Otherwise, input something like: `-pi/2, pi`.

3. **Number of sample points**:  
   - Higher numbers make smoother curves.
   - Leave blank for the default (1000 points).

4. **Filename to save the graph**:  
   - Example: `rose_curve.png`
   - If left blank, the script will auto-generate a filename based on the function.

---

## 🔹 Output

- Images are saved as `.png` files.
- They are:
  - **6 × 6 inches**
  - **300 DPI**
  - **Tightly cropped** (`bbox_inches='tight'`)
- Saved graphs are clean and ready for insertion into:
  - LaTeX (`\includegraphics`)
  - Canva
  - Google Slides
  - Word documents
  - Exam PDFs

---

## 🔹 Example Session

```plaintext
=== Polar Function Grapher ===
Type 'quit' at any prompt to exit.

Enter r(θ) = 3*sin(2*theta)
θ range (start,end in radians) [default 0,2π]: 
Number of sample points [default 1000]: 1500
Save as filename (e.g. 'rose.png') [leave blank to skip]: 
Saved plot to 'graph_3sin2theta.png'
```

The graph is saved automatically!

---

## 🔹 Limitations

- Currently only supports functions of \( r(\theta) \).
- Fixed θ plots (like \( \theta = \pi/4 \)) are **not yet implemented** (future feature).
- No GUI — runs entirely through command-line prompts.

---

## 🔹 Future Improvements (Optional)

- Add support for `theta = ...` (fixed radial lines).
- Batch processing of multiple functions.
- Auto-LaTeX document generation with graphs inserted.
- Graph style options (dashed, colored, annotations).

---

# 📚 Notes

- If an invalid expression is entered, the script will prompt you again.
- All images are saved relative to the project folder unless specified otherwise.

---

# ✅ Quick Commands Summary

| Action                     | Example                          |
|:----------------------------|:---------------------------------|
| Run script                  | `python PolarGraph.py`           |
| Function input              | `3*sin(2*theta)`                 |
| θ Range input               | `0,2*pi`                         |
| Sample points               | `1500`                           |
| Save file                   | `rose.png` or auto-named         |