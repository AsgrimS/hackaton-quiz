import {
  Box,
  Container,
  Divider,
  Link,
  Stack,
  Text,
  useColorModeValue,
} from "@chakra-ui/react";

export const Footer = () => {
  return (
    <Box
      bg={useColorModeValue("gray.50", "gray.900")}
      color={useColorModeValue("gray.700", "gray.200")}
    >
      <Container
        as={Stack}
        maxW={"6xl"}
        py={4}
        spacing={4}
        justify={"center"}
        align={"center"}
      >
        <Stack direction={"row"} spacing={6}>
          <Link href={"/"}>Home</Link>
          <Link href={"/leaderboards"}>Leaderboards</Link>
        </Stack>
        <Divider />
        <Text>© 2023 STX Next Hackaton. Your kwiz app</Text>
      </Container>
    </Box>
  );
};
