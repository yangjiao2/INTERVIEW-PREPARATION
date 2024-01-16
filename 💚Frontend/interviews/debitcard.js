import React from "react"
import "./DebitCard.css"
import cards from "../../cards.json"
import { useState } from "react"
export const DebitCard = () => {
	const [selectedCard, setSelectedCard] = useState(1);
	const [card, setCard] = useState(null);
	const [show, setShow] = useState(false);
	// {
	// 	"number":"4111111111111111",
	// 	"expiry":"12/25",
	// 	"cvv":"123",
	// 	"name":"JOHN DOE",
	// 	"bank":"Bank of HackerLand"
	// },
	const selectCard = (cardIndex) => {
		setSelectedCard(cardIndex);
		setCard(cards[selectedCard]);
	}

	return (
		<div className="mt-50 layout-column justify-content-center align-items-center" >
			<div className="card outlined" style={{ width: '1000px' }} 
				onClick={() => {setShow(prev => !prev)}}>
					{card ? (
					<div data-testid="debit-card">
						<h3 style={{ textAlign: 'center' }}>Card Details</h3>
						<br />
						<div className="debit-card-body" data-testid="debit-card-body">
							<p className="debit-card-bank" data-testid="debit-card-bank-name">{card.bank}</p>
							<p className="debit-card-no" data-testid="debit-card-no">{show ? card.number.match(/.{1,4}/g).join(' ') : `${card.number.substring(0, 4)} ${('X').repeat(4)} ${('X').repeat(4)} ${('X').repeat(4)}`}</p>
							<br />
							<div style={{ height: '45px', backgroundColor: 'black' }} className="debit-card-stripe"></div>
							<p>
								<span className="debit-card-holder-name" data-testid="debit-card-holder-name">{show ? card.name : card.name.split(" ").map(word => "XXXX").join(' ')}</span>
								<span className="debit-card-date" data-testid="debit-card-expiry-date">{show ? card.expiry : 'XX/XX'}</span>
								<span className="debit-card-cvv" data-testid="debit-card-cvv">{show? card.cvv : 'XXX'}</span></p>
						</div>
					</div>
					) : null}
				<div>
					<h3 style={{ textAlign: "center" }}>Cards List</h3>
					<div className="debit-card-list" data-testid="debit-card-list">

						{/* optimize to map: {card.map((card, index) => {})} */}
						<div className="list-card" data-testid="list-card-0">
							<p className="list-card-title" onClick={() => {selectCard(1)}}>Card 1</p>
						</div>
						<div className="list-card" data-testid="list-card-2"  onClick={() => {selectCard(2)}}><p className="list-card-title">Card 2</p></div>
						<div className="list-card" data-testid="list-card-3"  onClick={() => {selectCard(3)}}><p className="list-card-title">Card 3</p></div>
						<div className="list-card" data-testid="list-card-4"  onClick={() => {selectCard(4)}}><p className="list-card-title">Card 4</p></div>

					</div>
				</div>
			</div>
		</div>
	)
}