import * as React from "react";
import { SVGProps } from "react";

const SvgComponent = (props: SVGProps<SVGSVGElement>) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 625.56 247.16"
    {...props}
  >
    <path
      d="M625.56 0v129.78h-76.84a83.1 83.1 0 0 0-161.94 0h-79a83.12 83.12 0 0 0-163.11 5.91 83.28 83.28 0 0 0-1 12.82v67.67h28.23v31H0v-31h28.16V31H0V0h143.71v88.87A114.35 114.35 0 0 1 255 0h129.6v88.87A114.36 114.36 0 0 1 496 0Z"
      data-name="Layer 2"
    />
  </svg>
);

export { SvgComponent as RMLogo };
