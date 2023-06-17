import { API_URL } from "@/consts/api";
import { Box, Button, FormControl, FormLabel, Input } from "@chakra-ui/react";
import { useEffect, useState } from "react";

export default function Login() {
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");

  useEffect(() => {
    if (!!localStorage.getItem("token")) {
      window.location.href = "/";
    }
  }, []);

  const handleSubmit = async () => {
    if (username === "" || password === "") return;
    const response = await fetch(`${API_URL}/token/pair`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem("token", data.access);
      localStorage.setItem("username", data.username);
      window.location.href = "/";
    }
  };

  return (
    <FormControl display={{ base: "flex" }} flexDirection="column" gap="5">
      <Box>
        <FormLabel>Username</FormLabel>
        <Input
          required
          value={username}
          onChange={(e) => setusername(e.target.value)}
          isInvalid={username === ""}
        />
      </Box>
      <Box>
        <FormLabel>Password</FormLabel>
        <Input
          required
          value={password}
          onChange={(e) => setpassword(e.target.value)}
          isInvalid={password === ""}
          type="password"
        />
      </Box>

      <Button type="submit" colorScheme="blue" onClick={handleSubmit}>
        Login
      </Button>
    </FormControl>
  );
}
