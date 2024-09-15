import Logo from "../../../public/Logo.png";
import Image from "next/image";

export default function LogoTop() {
  return (
    <div className="absolute top-5 right-5">
      <Image src={Logo} alt="Logo" width={400} className="mb-8" />
    </div>
  );
}
