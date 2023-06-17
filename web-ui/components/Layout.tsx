import { Box } from "@chakra-ui/react";
import { ReactNode } from "react";
import { Navbar } from "./Navbar";

interface Props {
  children: ReactNode;
}

export const Layout = ({ children }: Props) => {
  return (
    <div>
      <Navbar />
      <main>
        <Box mx="auto" maxW="4xl" py={4}>
          {children}
        </Box>
      </main>
    </div>
  );
};
