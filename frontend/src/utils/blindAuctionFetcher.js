import fetch from 'unfetch';

const blindAuctionFetcher = (url) =>
	fetch('https://api.blind-auction.com/dev/' + url).then((r) => r.json());

export default blindAuctionFetcher;
