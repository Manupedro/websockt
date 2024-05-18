import React, { useState, useEffect } from 'react';
import { w3cwebsocket as W3CWebSocket } from "websocket";

function ChatComponent() {
  
  useEffect(() => {
    // Criar um objeto WebSocket
    const chatSocket = new W3CWebSocket('ws://127.0.0.1:8000/ws/socket-server/');
  
  // Lidar com o evento de abertura da conexão WebSocket
    chatSocket.onopen = () => {
    console.log('WebSocket connection established.');
    };
  }, []);
  


/**/
  return (
    <div>
      <h1>Lets chat!</h1>
    
    </div>
  );
}

export default ChatComponent;
