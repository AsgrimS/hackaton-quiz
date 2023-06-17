import type { AppProps } from "next/app";
import { ChakraProvider } from "@chakra-ui/react";
import { Inter } from "next/font/google";
import { Layout } from "@/components/Layout";
import { SessionProvider } from "next-auth/react";

const inter = Inter({ subsets: ["latin"] });

const App = ({ Component, pageProps: { session, ...pageProps } }: AppProps) => {
  return (
    <div className={inter.className}>
      <ChakraProvider>
        <SessionProvider session={session}>
          <Layout>
            <Component {...pageProps} />
          </Layout>
        </SessionProvider>
      </ChakraProvider>
    </div>
  );
};

export default App;
