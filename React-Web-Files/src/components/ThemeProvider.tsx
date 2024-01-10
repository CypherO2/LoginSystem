import { ReactNode, createContext } from "react";
import useTheme from "../hooks/useTheme";

interface ThemeContextType {
  theme: "light" | "dark";
  setTheme: (theme: "light" | "dark") => void;
}

export const ThemeContext = createContext<ThemeContextType | null>(null);

function ThemeProvider({ children }: { children: ReactNode }) {
  const { theme, setTheme } = useTheme();

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
export default ThemeProvider;
