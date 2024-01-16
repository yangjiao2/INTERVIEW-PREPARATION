import './App.css';
import 'h8k-components';

import React, { useState, useEffect } from 'react';
const title = "Bytedance Interview";

const App = () => {
    const [count, setCount] = useState(0);
    const [imgURL, setImgUrl] = useState("");
    const [breeds, setBreeds] = useState([]);
    const [breedimgs, setBreedImgs] = useState([]);
    const url = "https://dog.ceo/api/breeds/image/random";
    const url2 = "https://dog.ceo/api/breeds/list/all";
    const url3 = "https://dog.ceo/api/breed/affenpinscher/images/random";

    useEffect(() => {
        const response = fetch(url).then(
            res => res.json()).then(
                data => {
                    setImgUrl("");
                }
        );

    }, []);

    useEffect(() => {
        const response = fetch(url2).then(
            res => res.json()
        ).then(data => {
            setBreeds(data["message"]);

            const promises = Object.keys(data["message"]).map(
                breed => {
                    return fetch(`https://dog.ceo/api/breed/${breed}/images/random`).then(res => res.json());
                }
            );
            const res = Promise.all(promises).then(
                data => {
                    setBreedImgs(data);
                }
            );

        });

    }, []);

    // console.log(breedimgs);

    return (
        <div >
             {/* {breedimgs.map(img =>
                { 
                    console.log(img);
                return (<div><img src={img["message"]} /></div>);
             })} */}
        <ul>
            {Object.keys(breeds).slice(0, 3).map(
                (breed, i) => {
                    if (breeds[breed].length == 0){
                        let breedimg = "";
                        if (breedimgs[i]){
                 
                            breedimg = breedimgs[i]["message"]
                        }
              ["message"];
                        return (<div key={breed}>{i}  {breed}<img src={breedimg} /> </div>);
                    }
                    
                    return (
                            <ul>
                            {breeds[breed].map(
                                sub => {
                                    return (
                                        <li key={sub}>
                                            {sub}
                                       </li>
                                    );
                                }
                            )}
                            </ul>
                    )
                }
            )}
        </ul>

        </div>
    );
}

export default App;
