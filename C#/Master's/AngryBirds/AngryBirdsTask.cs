using System;

namespace AngryBirds
{
	public static class AngryBirdsTask
	{
		// Ниже — это XML документация, её использует ваша среда разработки, 
		// чтобы показывать подсказки по использованию методов. 
		// Но писать её естественно не обязательно.
		/// <param name="v">Начальная скорость</param>
		/// <param name="distance">Расстояние до цели</param>
		/// <returns>Угол прицеливания в радианах от 0 до Pi/2</returns>
		public static double FindSightAngle(double v, double distance)
		{
			// Из формулы дальности полёта:
			// distance = ((v_0)^2 * sin2a)/g --> a = arcsin((g * distance) / (v_0)^2) / 2
			double g = 9.8;
			return Math.Asin((g * distance) / (v * v)) / 2;
		}
	}
}