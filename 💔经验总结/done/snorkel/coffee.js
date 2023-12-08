import { useState, useRef, useEffect, useCallback } from 'react';

import './style.css';

const coffees = {
  mocha: 1,
  chai: 2,
  latte: 4,
  matcha: 5,
};

export const App = () => {
  const [orders, setOrders] = useState<Record<string, any>>({});
  const [counters, setCounters] = useState({});
  const job = useRef(null);

  useEffect(() => {
    if (Object.keys(orders).length > 0 && !job.current) {
      // remove one order
      const drink = Object.keys(orders)[0];
      // assign order to job, start working

      // clear working status
      job.current = setTimeout(() => {
        job.current = null;
        console.log('clearTimeout job.current', job.current);

        // add to counter
        setCounters((prevcounter) => {
          // console.log('prevcounter[drink]', prevcounter[drink]);
          return {
            ...prevcounter,
            [drink]: (prevcounter[drink] || 0) + 1,
          };
        });
      }, coffees[drink] * 1000);

      setOrders((prevorders) => {
        const count = prevorders[drink];
        if (count == 1) {
          const { [drink]: _, ...newOrders } = prevorders;
          return newOrders;
        } else {
          return {
            ...prevorders,
            [drink]: count - 1,
          };
        }
      });
    }
  }, [orders, counters, job, setOrders, setCounters]);

  useEffect(() => {
    return () => {
      console.log('return job.current', job.current);

      if (job.current) {
        clearTimeout(job.current);
      }
    };
  }, []);
  const updateOrder = useCallback(
    (drink, value = null) => {
      const count = orders[drink];
      console.log('updateOrder', drink, count);
      // parseInt(undefined) >= 0  >> false
      if (count >= 0) {
        setOrders((prev) => {
          return {
            ...prev,
            [drink]: value,
          };
        });
      } else {
        setOrders((prev) => {
          return {
            ...prev,
            [drink]: 1,
          };
        });
      }
    },
    [orders, setOrders]
  );

  return (
    <div>
      <Menu
        title={'menu'}
        items={coffees}
        updateItem={(key) => updateOrder(key, orders[key] + 1)}
      />
      <Menu title={'order'} items={orders} displayValue={true} />
      <Menu title={'counter'} items={counters} displayValue={true} />
    </div>
  );
};

const Menu = ({
  updateItem = (key) => {},
  title = 'title',
  items = {},
  displayValue = false,
}) => {
  const renderTitle = (title) => {
    return <h1 className="title">{title}</h1>;
  };

  return (
    <div className="container">
      {renderTitle(title)}
      <ul>
        {Object.entries(items).map(([key, value]) => {
          return (
            <ListItem
              key={key}
              name={key}
              value={displayValue ? value : ' '}
              onClick={updateItem}
            />
          );
        })}
      </ul>
    </div>
  );
};

const ListItem = ({ name, value, onClick }) => {
  return (
    <li className="item" onClick={() => onClick(name)}>
      {name} {value}{' '}
    </li>
  );
};
