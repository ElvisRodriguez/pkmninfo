const AudioPlayer = ({url}) => {
  return (
    <div>
      <audio controls>
        <source src={url} type="audio/ogg" />
      </audio>
    </div>
  );
};

export default AudioPlayer;