import type { AppProps } from "next/app";
import { ChakraProvider } from "@chakra-ui/react";
import { Inter } from "next/font/google";
import { Layout } from "@/components/Layout";

const inter = Inter({ subsets: ["latin"] });

const App = ({ Component, pageProps }: AppProps) => {
  return (
    <div className={inter.className}>
      <ChakraProvider>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </ChakraProvider>
    </div>
  );
};

export default App;
