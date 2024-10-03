import { useState, useEffect } from "react";
import { getGameSegments } from "./dataService";

interface GameSegment {
  header: string;
  entries: any[];
}

// Use Record to define GameSegmentsData with dynamic keys
type GameSegmentsData = Record<string, GameSegment>;

const GameSegments = () => {
  const [data, setData] = useState<GameSegmentsData>({});

  useEffect(() => {
    const jsonData = getGameSegments(); // Get JSON data from utility
    setData(jsonData);
  }, []); // Runs once when component is mounted

  return (
    <div>
      {Object.keys(data).map((key) => (
        <div key={key}>
          <h1>{data[key].header}</h1>
          {data[key].entries.map((entry) => (
            <div>
              <p key={entry.id}>
                <input type="checkbox" />
                {entry.name}: {entry.description}
              </p>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default GameSegments;
