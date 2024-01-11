import { Container } from "react-bootstrap";
import { Routes, Route } from "react-router-dom";
import LoginForm from "./components/LoginForm";
import SignupForm from "./components/SignUpFrom";
import { INDEX_PATH, LOGIN_PATH, SIGNUP_PATH } from "./constants/paths";
function App() {
  return (
    <>
      <Container>
        <Routes>
          <Route path={INDEX_PATH} element={<LoginForm/>}/>
          <Route path={SIGNUP_PATH} element={<SignupForm />} />
          <Route path={LOGIN_PATH} element={<LoginForm />} />
        </Routes>
      </Container>
    </>
  );
}

export default App;
