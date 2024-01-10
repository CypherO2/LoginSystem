import { useState } from "react";

function useTheme() {
  const storedTheme = localStorage.getItem("theme");

  const [theme, setTheme] = useState<"light" | "dark">(
    storedTheme === "dark" ? storedTheme : "light"
  );

  const saveTheme = (theme: "light" | "dark") => {
    localStorage.setItem("theme", theme);
    setTheme(theme);
  };

  return { theme, setTheme: saveTheme };
}

export default useTheme;
