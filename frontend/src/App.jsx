import React from 'react';

function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Hệ Thống Quản Lý Dự Án Nhóm (AI Integrated)</h1>
      <p>Giao diện ReactJS - Kanban Board & AI Assistant</p>
    </div>
  );
}

export default App;

// Component Kanban Board
export function KanbanBoard() {
  return <div className="board">Kanban Task Board</div>;
}
