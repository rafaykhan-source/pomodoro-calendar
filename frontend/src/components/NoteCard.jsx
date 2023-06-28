import {
  Card,
  CardBody,
  Typography,
  Button,
  Textarea,
} from "@material-tailwind/react";

function NoteCard() {
  return (
    <>
        <Card className="flex w-full max-w-[20rem] outline-slate-800r">
          <CardBody>
            <Typography variant="h4" className="uppercase mb-4">
              Title
            </Typography>
            <Textarea className="flex text-black" color="red" label="test" />
            <a href="#" className="inline-block">
              <Button className="bg-[#ee4e22] hover:bg-[#8f2d12] flex items-center gap-2 py-2 px-4 rounded">
                Submit
              </Button>
            </a>
          </CardBody>
        </Card>
    </>
  );
}

export default NoteCard;
