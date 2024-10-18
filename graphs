import React from 'react';
import { ResponsiveContainer, Tooltip } from 'recharts';

const data = [
  { variable: 'RSMI', RSMI: 1, CSMI: 0.642, BSMI: 0.587, ISMI: 0.534, OP: 0.768, GP: 0.589 },
  { variable: 'CSMI', RSMI: 0.642, CSMI: 1, BSMI: 0.623, ISMI: 0.698, OP: 0.523, GP: 0.412 },
  { variable: 'BSMI', RSMI: 0.587, CSMI: 0.623, BSMI: 1, ISMI: 0.612, OP: 0.645, GP: 0.501 },
  { variable: 'ISMI', RSMI: 0.534, CSMI: 0.698, BSMI: 0.612, ISMI: 1, OP: 0.489, GP: 0.378 },
  { variable: 'OP', RSMI: 0.768, CSMI: 0.523, BSMI: 0.645, ISMI: 0.489, OP: 1, GP: 0.701 },
  { variable: 'GP', RSMI: 0.589, CSMI: 0.412, BSMI: 0.501, ISMI: 0.378, GP: 0.701, GP: 1 },
];

const CellContent = ({ value }) => (
  <div style={{
    width: '100%',
    height: '100%',
    backgroundColor: `rgba(0, 0, 255, ${value})`,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    color: value > 0.5 ? 'white' : 'black'
  }}>
    {value.toFixed(3)}
  </div>
);

const Heatmap = () => (
  <ResponsiveContainer width="100%" height={400}>
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)' }}>
      <div></div>
      {['RSMI', 'CSMI', 'BSMI', 'ISMI', 'OP', 'GP'].map(header => (
        <div key={header} style={{ textAlign: 'center', fontWeight: 'bold' }}>{header}</div>
      ))}
      {data.map(row => (
        <>
          <div style={{ fontWeight: 'bold' }}>{row.variable}</div>
          {['RSMI', 'CSMI', 'BSMI', 'ISMI', 'OP', 'GP'].map(variable => (
            <CellContent key={variable} value={row[variable]} />
          ))}
        </>
      ))}
    </div>
  </ResponsiveContainer>
);

export default Heatmap;
