import React from "react";
import { View, Text } from "react-native";

export default function App() {
  console.log("APP RENDER");

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Daftar Mahasiswa</Text>
    </View>
  );
}
