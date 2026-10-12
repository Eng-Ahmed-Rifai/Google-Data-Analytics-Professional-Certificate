# Course 7 Study Guide & Verified Quiz Solutions: Data Analysis with R Programming

**Course 7:** Data Analysis with R Programming  
**Specialization:** Google Data Analytics Professional Certificate  
**Learner:** Eng. Ahmed Rifai  
**Verified Grade:** 100.00% Perfect Score  
**Credential Verification:** [Coursera Accomplishment Record VH868ASXMQGV](https://www.coursera.org/account/accomplishments/verify/VH868ASXMQGV)  

---

## 1. Key Conceptual Pillars & R Code Patterns

### 1.1 Tidyverse Core Packages
- **`ggplot2`**: Data visualization based on the Grammar of Graphics.
- **`dplyr`**: Data manipulation grammar (`filter`, `select`, `mutate`, `arrange`, `summarize`, `group_by`).
- **`tidyr`**: Data tidying (`pivot_longer`, `pivot_wider`, `separate`, `unite`).
- **`readr`**: High-performance rectangular data import (`read_csv`).
- **`tibble`**: Modern re-imagining of data frames with refined printing and subsetting.
- **`purrr`**: Functional programming toolkit.
- **`stringr`**: String manipulation functions.
- **`forcats`**: Categorical variable (factor) handling.

### 1.2 Essential dplyr Transformations
```r
library(tidyverse)

# End-to-end data processing with pipes
cleaned_data <- raw_data %>%
  # 1. Filter rows
  filter(!is.na(salary) & age >= 21) %>%
  # 2. Select and rename columns
  select(employee_id = id, department, salary, hire_date) %>%
  # 3. Create derived columns
  mutate(salary_k = salary / 1000,
         experience_years = as.numeric(difftime(Sys.Date(), hire_date, units = "weeks")) / 52.25) %>%
  # 4. Group and summarize
  group_by(department) %>%
  summarize(
    headcount = n(),
    avg_salary = mean(salary, na.rm = TRUE),
    median_salary = median(salary, na.rm = TRUE)
  ) %>%
  # 5. Sort descending
  arrange(desc(avg_salary))
```

### 1.3 Grammar of Graphics with ggplot2
```r
# Core ggplot2 layer anatomy
ggplot(data = diamonds, mapping = aes(x = carat, y = price, color = cut)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE) +
  facet_wrap(~ clarity) +
  labs(
    title = "Diamond Price vs. Carat Weight by Clarity",
    subtitle = "Analysis of cut quality and price scaling",
    x = "Carat Weight",
    y = "Price ($ USD)",
    color = "Cut Grade",
    caption = "Source: ggplot2 diamonds dataset"
  ) +
  theme_minimal()
```

---

## 2. 100% Verified Quiz Solutions Bank

### Question 1 (Module 1)
**What is the primary difference between a vector and a list in R?**
- **Answer:** A vector must contain elements of the exact same data type (homogeneous), whereas a list can contain elements of different data types, including vectors, strings, matrices, or other lists (heterogeneous).
- **Rationale:** In R, atomic vectors are strictly homogeneous. If you combine different types, R performs implicit coercion. Lists preserve distinct element types without coercion.

### Question 2 (Module 2)
**Which operator in R is used to pass the output of one function directly into the first argument of the next function?**
- **Answer:** The pipe operator `%>%` (from `magrittr` / `tidyverse`) or the native pipe `|>` (R 4.1+).
- **Rationale:** The pipe operator eliminates nested function calls and temporary intermediate variables, significantly improving code readability and debugging flow.

### Question 3 (Module 3)
**Which `dplyr` function should you use to sort rows of a data frame based on values in one or more columns?**
- **Answer:** `arrange()` (or `arrange(desc(column))` for descending order).
- **Rationale:** `arrange()` reorders the rows of a data frame according to the specified variables. `sort()` is for atomic vectors, while `order()` is base R syntax.

### Question 4 (Module 4)
**In `ggplot2`, which layer is responsible for creating separate visual subplots for each category of a categorical variable?**
- **Answer:** `facet_wrap()` or `facet_grid()`.
- **Rationale:** Faceting splits a plot into a matrix of smaller panels, displaying a different subset of data in each pane based on categorical grouping.

### Question 5 (Module 5)
**In an R Markdown document, which chunk option ensures that code runs and displays its output, but prevents the raw R code from appearing in the final rendered document?**
- **Answer:** `echo = FALSE`
- **Rationale:** Setting `echo = FALSE` in `{r echo = FALSE}` suppresses the code display while allowing the output (tables, graphs, text results) to render cleanly, which is the standard for executive reports.
