type Props = {
    searchTerm: string;
    onDeleteSearch: () => void;
    onSearchChange: (searchTerm: string) => void;
    onSearchClick: () => void;

};


const SearchBar = {(searchTerm, onDeleteSearch, onSearchChange, onSearchClick ,): Props} => {

    return <div>
        <Button onClick={onDeleteSearch}>Delete</Button>

        <input
            value={searchTerm}
            onChange={()}
    </div>
}