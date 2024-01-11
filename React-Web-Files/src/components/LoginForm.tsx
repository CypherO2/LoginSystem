import { FormEvent, useContext, useState } from "react";
import { ThemeContext } from "./ThemeProvider";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
} from "mdb-react-ui-kit";
import { Button, Col, Form, Row } from "react-bootstrap";
import axios from "axios";
function LoginForm() {
  const themeContext = useContext(ThemeContext);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [responseText, setResponseText] = useState("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setResponseText("");

    try {
      const response = await axios.post("https://localhost:5000/login", {
        username: username,
        password: password,
      });
      setResponseText(JSON.stringify(response.data));
    } catch (error) {
      if (axios.isAxiosError(error)) {
        setResponseText(error.message);
      } else {
        setResponseText(String(error));
      }
    }
  };

  return (
    <>
      <Row>
        <Col className="my-5 py-5" />
      </Row>
      <MDBContainer fluid bgColor={themeContext?.theme}>
        <MDBRow className="d-flex justify-content-center align-items-center h-100">
          <MDBCol col="12">
            <MDBCard
              className="bg-dark text-white my-5 mx-auto"
              style={{ borderRadius: "1rem", maxWidth: "400px" }}
            >
              <MDBCardBody className="p-5 mb-5 d-flex flex-column align-items-center mx-auto w-100">
                <h2 className="fw-bold mb-2 text-uppercase">Login</h2>
                <p className="text-white-50 mb-5">
                  Please enter your login and password!
                </p>

                <Form onSubmit={handleSubmit}>
                  <Form.Group className="" controlId="formBasicEmail">
                    <Form.Label>Username</Form.Label>
                    <Form.Control
                      id="username"
                      type="text"
                      placeholder="Enter email"
                      onChange={(e) => setUsername(e.target.value)}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                      id="password"
                      type="password"
                      placeholder="Password"
                      onChange={(e) => setPassword(e.target.value)}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3" controlId="formBasicCheckbox">
                    <Form.Check type="checkbox" label="Remember Me" />
                  </Form.Group>
                  <Row>
                    <Col className="d-grid gap-2">
                      <Button
                        variant="dark"
                        type="submit"
                        className="border border-light "
                      >
                        Login
                      </Button>
                    </Col>
                  </Row>
                  {responseText && (
                    <p className="text-white">Response: {responseText}</p>
                  )}
                  <Row>
                    <Col>
                      <p>
                        Don't have an account?{" "}
                        <a href="/signup" className="text-primary">
                          Create one
                        </a>
                      </p>
                    </Col>
                  </Row>
                </Form>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </>
  );
}
export default LoginForm;
