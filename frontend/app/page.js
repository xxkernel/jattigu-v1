import PricingPage from './_pages/PricingPage';
import FigurePage from './_pages/FigurePage';
import HomePage from './_pages/HomePage';
import WayChoosePage from './_pages/WayChoosePage';
import FooterPage from './_pages/FooterPage';

export default function Home() {
  return (
    <div className="bg-white">
      <HomePage />
      <FigurePage />
      <WayChoosePage />
      <PricingPage />
      <FooterPage />
    </div>
  );
}
