import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";

export const authOptions = {
  providers: [
    CredentialsProvider({
      name: "password",
      credentials: {
        username: {
          label: "User",
          type: "text",
          placeholder: "Username",
        },
        password: {
          label: "Password",
          type: "password",
          placeholder: "Password",
        },
      },

      async authorize(credentials, req) {
        if (!credentials) {
          throw new Error("Brak danych logowania");
        }

        if (!credentials.username || !credentials.password) {
          throw new Error("Email i hasło są wymagane");
        }

        if (!(credentials.username === "test")) {
          throw new Error("Nieprawidłowy email lub hasło");
        }

        return { id: 1, name: "Test User" };
      },
    }),
  ],
};
export default NextAuth(authOptions);
