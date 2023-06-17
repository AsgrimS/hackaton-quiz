import { Box } from "@chakra-ui/react";
import { ReactNode } from "react";
import { Footer } from "./Footer";
import { Navbar } from "./Navbar";

interface Props {
  children: ReactNode;
}

export const Layout = ({ children }: Props) => {
  return (
    <Box display={{ base: "flex" }} flexDir="column" minH="100vh">
      <Box flexGrow="1">
        <Navbar />
        <main>
          <Box mx="auto" maxW="4xl" py={4}>
            {children}
          </Box>
        </main>
      </Box>
      <Footer />
    </Box>
  );
};
