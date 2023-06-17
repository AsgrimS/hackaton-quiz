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

        const response = await fetch(`${process.env.NEXT_API_URL}/token/pair`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: credentials.username,
            password: credentials.password,
          }),
        });

        const data = await response.json();

        return { ...data, name: data.username };
      },
    }),
  ],
};
export default NextAuth(authOptions);
