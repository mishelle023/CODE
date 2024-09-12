type Props = {
    onClick: () => void;
    title: string;
};

function Button({ title, onClick }: Props) {

    return <button onClick={onClick}>{title}</button>;
}