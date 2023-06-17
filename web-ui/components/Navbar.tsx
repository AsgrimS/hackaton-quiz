import { ChevronRightIcon, PlusSquareIcon } from "@chakra-ui/icons";
import {
  Box,
  Button,
  Flex,
  Icon,
  Link,
  Popover,
  PopoverContent,
  PopoverTrigger,
  Stack,
  Text,
  useBreakpointValue,
  useColorModeValue,
} from "@chakra-ui/react";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export const Navbar = () => {
  const [token, setToken] = useState("");
  const [username, setUsername] = useState("");

  useEffect(() => {
    if (!!localStorage.getItem("token")) {
      setToken(localStorage.getItem("token") || "");
      setUsername(localStorage.getItem("username") || "");
    }
  }, []);

  return (
    <Box>
      <Flex
        bg={useColorModeValue("white", "gray.800")}
        color={useColorModeValue("gray.600", "white")}
        minH={"60px"}
        py={{ base: 2 }}
        px={{ base: 4 }}
        borderBottom={1}
        borderStyle={"solid"}
        borderColor={useColorModeValue("gray.200", "gray.900")}
        align={"center"}
      >
        <Flex
          flex={{ base: 1 }}
          justify={{ base: "center", md: "start" }}
          align="center"
        >
          <Text
            textAlign={useBreakpointValue({ base: "center", md: "left" })}
            fontFamily={"heading"}
            color={useColorModeValue("gray.800", "white")}
          >
            Your kwiz
          </Text>

          <Flex display={{ base: "none", md: "flex" }} ml={10}>
            <DesktopNav />
          </Flex>
        </Flex>

        <Stack
          flex={{ base: 1 }}
          justify={"flex-end"}
          direction={"row"}
          spacing={6}
        >
          {!!token ? (
            <Box display={{ base: "flex" }}>
              <Text display={{ base: "flex" }} alignItems="center" mr="4">
                Logged in as {username}
              </Text>
              <Button
                as={"a"}
                fontSize={"sm"}
                fontWeight={600}
                color={"white"}
                bg={"pink.400"}
                _hover={{
                  bg: "pink.300",
                }}
                onClick={() => {
                  localStorage.removeItem("token");
                  localStorage.removeItem("username");
                  window.location.href = "/";
                }}
              >
                Sign Out
              </Button>
            </Box>
          ) : (
            <Button
              as={"a"}
              display={{ base: "none", md: "inline-flex" }}
              fontSize={"sm"}
              fontWeight={600}
              color={"white"}
              bg={"pink.400"}
              href={"/login"}
              _hover={{
                bg: "pink.300",
              }}
            >
              Sign In
            </Button>
          )}
        </Stack>
      </Flex>
    </Box>
  );
};

const DesktopNav = () => {
  const linkColor = useColorModeValue("gray.600", "gray.200");
  const linkHoverColor = useColorModeValue("gray.800", "white");
  const popoverContentBgColor = useColorModeValue("white", "gray.800");
  const router = useRouter();
  const [token, setToken] = useState("");
  const [username, setUsername] = useState("");

  useEffect(() => {
    if (!!localStorage.getItem("token")) {
      setToken(localStorage.getItem("token") || "");
      setUsername(localStorage.getItem("username") || "");
    }
  }, []);

  return (
    <Stack direction={"row"} spacing={4} alignItems="center">
      {NAV_ITEMS.map((navItem) => (
        <Box key={navItem.label}>
          <Popover trigger={"hover"} placement={"bottom-start"}>
            <PopoverTrigger>
              <Link
                p={2}
                href={navItem.href ?? "#"}
                fontSize={"sm"}
                fontWeight={500}
                color={linkColor}
                _hover={{
                  textDecoration: "none",
                  color: linkHoverColor,
                }}
              >
                {navItem.label}
              </Link>
            </PopoverTrigger>

            {navItem.children && (
              <PopoverContent
                border={0}
                boxShadow={"xl"}
                bg={popoverContentBgColor}
                p={4}
                rounded={"xl"}
                minW={"sm"}
              >
                <Stack>
                  {navItem.children.map((child) => (
                    <DesktopSubNav key={child.label} {...child} />
                  ))}
                </Stack>
              </PopoverContent>
            )}
          </Popover>
        </Box>
      ))}
      {!(router.pathname === "/create-quiz") && !!token && (
        <Button
          as={"a"}
          display={{ base: "flex", md: "inline-flex" }}
          fontSize={"sm"}
          fontWeight={600}
          colorScheme="blue"
          alignItems="center"
          href="/create-quiz"
        >
          <PlusSquareIcon />
          <Text ml="1">Create new quiz</Text>
        </Button>
      )}
    </Stack>
  );
};

const DesktopSubNav = ({ label, href, subLabel }: NavItem) => {
  return (
    <Link
      href={href}
      role={"group"}
      display={"block"}
      p={2}
      rounded={"md"}
      _hover={{ bg: useColorModeValue("pink.50", "gray.900") }}
    >
      <Stack direction={"row"} align={"center"}>
        <Box>
          <Text
            transition={"all .3s ease"}
            _groupHover={{ color: "pink.400" }}
            fontWeight={500}
          >
            {label}
          </Text>
          <Text fontSize={"sm"}>{subLabel}</Text>
        </Box>
        <Flex
          transition={"all .3s ease"}
          transform={"translateX(-10px)"}
          opacity={0}
          _groupHover={{ opacity: "100%", transform: "translateX(0)" }}
          justify={"flex-end"}
          align={"center"}
          flex={1}
        >
          <Icon color={"pink.400"} w={5} h={5} as={ChevronRightIcon} />
        </Flex>
      </Stack>
    </Link>
  );
};

interface NavItem {
  label: string;
  subLabel?: string;
  children?: Array<NavItem>;
  href?: string;
}

const NAV_ITEMS: Array<NavItem> = [
  {
    label: "Home",
    href: "/",
  },
  {
    label: "Leaderboards",
    href: "/leaderboards",
  },
];
