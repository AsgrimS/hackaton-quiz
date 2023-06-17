import { LeaderBoardEntry } from "@/common/interfaces";
import { fetcher } from "@/common/utils";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
  Heading,
  Spinner,
} from "@chakra-ui/react";

import userSWR from "swr";

export const Leaderboard = (props: { quizId: number }) => {
  const { data, error } = userSWR<LeaderBoardEntry[]>(
    `http://localhost:8000/api/leaderboard/${props.quizId}`,
    fetcher
  );

  if (error) return <div>failed to load</div>;

  if (!data) return <Spinner />;

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
              <Th>Score</Th>
              <Th isNumeric>Time</Th>
            </Tr>
          </Thead>
          <Tbody>
            {data.map((entry, key) => (
              <Tr key={key}>
                <Td>{entry.place}</Td>
                <Td>{entry.username}</Td>
                <Td>{entry.score}%</Td>
                <Td isNumeric>{entry.time}</Td>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </TableContainer>
    </section>
  );
};
