let allSeats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

let preferredSeats = {
  Earthenware: [1, 12, 2, 11, 3],
  Waterfall: [4, 3, 5, 2, 6],
  Fireplace: [7, 6, 8, 5, 9],
  Windowsill: [10, 9, 11, 8, 12],
};

function ghostSeats(ghostName) {
  function findClan(name) {
    const ghostClans = [
      { clan: "Earthenware", value: "QUTHCRDMZ" },
      { clan: "Waterfall", value: "WEVOXING" },
      { clan: "Fireplace", value: "JFABKPLY" },
      { clan: "Windowsill", value: "SSSSSSSSS" },
    ];
    const firstLetter = name[0].toUpperCase();

    return ghostClans.find((obj) =>
      obj.value.toUpperCase().includes(firstLetter)
    )?.clan;
  }

  const clan = findClan(ghostName);
  if (!clan) return;

  const clanSeats = preferredSeats[clan];
  if (!clanSeats || clanSeats.length === 0) return;

   const indexToRemove = clanSeats.indexOf(
    clanSeats.find((seat) => allSeats.includes(seat))
  );
  const removedSeat = clanSeats.splice(indexToRemove, 1)[0]; 
  allSeats = allSeats.filter((seat) => seat !== removedSeat); 

  const rotatedSeats = [
    ...clanSeats.slice(indexToRemove),
    ...clanSeats.slice(0, indexToRemove),
  ];
  preferredSeats[clan] = rotatedSeats;

  return {
    remainingSeats: allSeats,
    remainingPreferredSeats: preferredSeats,
    ghostSeatedAt: removedSeat,
  };
}

ghostNames = ["Ali", "Saba", "Wino", "Utha", "Baba", "Suna"];

function processGhostNames(ghostNames, callback) {
  const resultsContainer = document.getElementById("results-container");

  ghostNames.forEach((ghostName) => {
    const result = callback(ghostName);
    if (result) {
      const resultH1Element = document.createElement("h1");
      resultH1Element.textContent = `Ghost: ${ghostName}`
      const resultH4Element = document.createElement("h4");
      resultH4Element.textContent = `Seated at: ${result.ghostSeatedAt}. Remaining Seats: ${result.remainingSeats}`;
      resultsContainer.appendChild(resultH1Element);
      resultsContainer.appendChild(resultH4Element);
    }
  });
}

processGhostNames(ghostNames, ghostSeats);