// https://codesandbox.io/s/zen-snow-zl47ey?file=/src/App.js

/**
 * Challenge: Create an exchange rate card. Fulfill user stories below:
 * User story: I can see USD to JPY as my currencty exchange default.
 * User story: I can see latest current exchange rate in the outlined box.
 * User story: I can choose other currencies to see the current rates
 *             by clicking on the dropdown icon.
 * User story: I can switch between my chosen currencies by clicking
 *             on the exchange icon (in blue).
 * User story: I can enter the amount of money like 5,893 USD and see the
 *             equivalent amount in other currencies.
 * User story: I can see updated date in Pacific time zone.
 * api for list of currencies: https://api.coinbase.com/v2/currencies
 * api for the exchange rate: https://open.er-api.com/v6/latest/EUR
 * Substitute `EUR` with the code you want to use as a base currency.
 */
import { useState, useRef, useMemo, useEffect, useCallback } from "react";
import "./styles.css";

export default function App() {
    const [cur1, setCur1] = useState("EUR");
    const [cur2, setCur2] = useState("USD");

    const [currencies, setCurrencies] = useState([]);
    const [rates, setRates] = useState(0);

    const [cur1val, setCur1val] = useState(1);
    const [cur2val, setCur2val] = useState(null);

    const timestamp = useRef(null);

    useEffect(() => {
        fetch("https://api.coinbase.com/v2/currencies")
            .then((val) => {
                return val.json();
            })
            .then((res) => {
                setCurrencies(res.data.map((e) => e["id"]));
            });
    }, []);

    useEffect(() => {
        fetch("https://open.er-api.com/v6/latest/" + cur1)
            .then((val) => {
                console.log(val);
                return val.json();
            })
            .then((res) => {
                let last_update_timestamp = res.time_last_update_utc;
                setRates(res.rates);
                // setCur2val(cur1val * res.rates[cur2]);
                timestamp.current = last_update_timestamp;
            });
    }, [cur1, cur2]);
    // console.log('currencies',currencies, rates, cur1, timestamp.current);

    const rate = rates[cur2];

    return (
        <div className="App">
            <div className="container">
                <div className="currency">
                    <select
                        id="from_currency"
                        onSelect={(e) => {
                            setCur1(e.target.value);
                        }}
                    >
                        <option value={cur1} selected>
                            {cur1}
                        </option>
                        {currencies
                            .filter((c) => c !== cur1)
                            .map((c) => {
                                return <option value={c}>{c}</option>;
                            })}
                    </select>
                    <input
                        type="number"
                        id="from_ammount"
                        placeholder="0"
                        value={cur1val}
                        onChange={(e) => {
                            setCur1val(e.target.val);
                            setCur2val(e.target.value * rate);
                        }}
                    />
                </div>
                <div className="middle">
                    <button
                        id="exchange"
                        onClick={(e) => {
                            let tmpcur1 = cur1;
                            let tmpcur2 = cur2;
                            setCur1(tmpcur2);
                            setCur2(tmpcur1);
                        }}
                    >
                        <i className="fas fa-exchange-alt"></i>
                    </button>
                    <div className="rate" id="rate">
                        1 {cur1} = {rate} {cur2}
                    </div>
                </div>
                <div className="currency">
                    <select
                        id="to_currency"
                        onSelect={(e) => {
                            setCur2(e.target.value);
                        }}
                    >
                        <option value={cur2} selected>
                            {cur2}
                        </option>
                        {currencies
                            .filter((c) => c !== cur2)
                            .map((c) => {
                                return <option value={c}>{c}</option>;
                            })}
                    </select>
                    <input
                        type="number"
                        id="to_ammount"
                        placeholder="0"
                        value={cur2val}
                        onChange={(e) => {
                            setCur2val(e.target.val);
                            setCur1val(e.target.value / rate);
                        }}
                    />
                </div>
                <div className="date">{timestamp.current}</div>
            </div>
        </div>
    );
}
