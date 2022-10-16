import useGetItems from '../hooks/useGetItems';
import ItemCardGrid from './ItemCardGrid';

const Items = () => {
	const items = useGetItems();
	return <ItemCardGrid items={items} />;
};
export default Items;
