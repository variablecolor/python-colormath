from colormathfive.color_objects import SpectralColor as SpectralColorFive
from colormathfive.color_objects import XYZColor as XYZColorFive
from colormathfive.color_objects import LabColor as LabColorFive
from colormathfive.color_conversions import convert_color as convert_colorFive

test_cases = [("d50", "2"),
              ("d50", "10"),
              ("d65", "10"),
              ("d65", "2"),
              ("a", "2"),
              ("a", "10"),
              ("b", "2"),
              ("b", "10"),
              ("c", "2"),
              ("c", "10"),
              ("f2", "10"),
              ("f2", "2"),
              ("f7", "10"),
              ("f7", "2"),
              ("f11", "10"),
              ("f11", "2")]


def prediction_to_lab_color_custom_five(color_row, illum, observer):
    """
    Both ANNOne and ANNTwo have the same output format, a reflectance curve on a 0-1 scale across 31 points (400-700nm).

    Since reference data for both of these ANNs is in d65 10deg, I consider the predictions d65 10deg.

    This function converts a single prediction to d65 10deg Lab space.

    Returns a colormath Lab Object.
    """

    args = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] + color_row + [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, observer, illum]

    spectral_color = SpectralColorFive(*args)

    xyz_color = convert_colorFive(spectral_color, target_cs=XYZColorFive)

    lab_color = convert_colorFive(xyz_color, target_cs=LabColorFive)

    return lab_color


def run_tests_to_lab(spectral_curve, test_case_tuple_list):

    for t_c in test_case_tuple_list:

        lab = prediction_to_lab_color_custom_five(spectral_curve, t_c[0], t_c[1])

        print("{}/{} {}".format(t_c[0], t_c[1], lab.get_value_tuple(), lab.illuminant, lab.observer))


def interpolate_yolo_cats(spectral_input_curve):
    """
    Takes a 400-700nm spectral curve @ 10nm resolution as input.
    """

    five_curve = []

    for i_s in range(len(spectral_input_curve)):

        if i_s != (len(spectral_input_curve) - 1):

            i_e = i_s + 1

            five_curve.append(spectral_input_curve[i_s])

            interpolated_curve = (spectral_input_curve[i_s] + spectral_input_curve[i_e]) / 2.0

            five_curve.append(interpolated_curve)

        else:

            five_curve.append(spectral_input_curve[i_s])

    return five_curve


if __name__ == '__main__':

    spectral_curve = [0.50153, 0.80662, 0.93925, 0.95366, 0.94559, 0.93436, 0.93140, 0.93381, 0.94226, 0.94820,
		0.94834, 0.94735, 0.94894, 0.94841, 0.94646, 0.94034, 0.93470, 0.93526, 0.941164, 0.95054,
		0.95362, 0.95231, 0.94980, 0.95089, 0.95478, 0.95980, 0.96378, 0.96439, 0.964944, 0.96968, 0.97236]

    five_curve = interpolate_yolo_cats(spectral_curve)

    run_tests_to_lab(five_curve, test_cases)