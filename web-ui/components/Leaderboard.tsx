import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
  Heading,
} from "@chakra-ui/react";

export const Leaderboard = () => {
  return (
    <section>
      <Heading textAlign="center" p={10}>
        Quiz Title Leaderboard
      </Heading>
      <TableContainer>
        <Table variant="simple">
          <Thead>
            <Tr>
              <Th>Place</Th>
              <Th>User name</Th>
              <Th>Points</Th>
              <Th isNumeric>Time</Th>
            </Tr>
          </Thead>
          <Tbody>
            <Tr>
              <Td>1</Td>
              <Td>Luke The</Td>
              <Td>10</Td>
              <Td isNumeric>25:33</Td>
            </Tr>
            <Tr>
              <Td>1</Td>
              <Td>Luke The</Td>
              <Td>10</Td>
              <Td isNumeric>25:33</Td>
            </Tr>
            <Tr>
              <Td>1</Td>
              <Td>Luke The</Td>
              <Td>10</Td>
              <Td isNumeric>25:33</Td>
            </Tr>
            <Tr>
              <Td>1</Td>
              <Td>Luke The</Td>
              <Td>10</Td>
              <Td isNumeric>25:33</Td>
            </Tr>
          </Tbody>
        </Table>
      </TableContainer>
    </section>
  );
};
